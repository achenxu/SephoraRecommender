<template>
  <div id="app">
    <div class="container">
      <!--UPLOAD-->
      <form enctype="multipart/form-data" novalidate v-if="isInitial || isSaving">
        <h1>Sephora Recommender</h1>
        <div class="dropbox">
          <input type="file" :name="uploadFieldName" :disabled="isSaving" @change="filesChange($event.target.name, $event.target.files); fileCount = $event.target.files.length" accept="image/*" class="input-file">
            <p v-if="isInitial">
              Drag your image here or click to choose one
            </p>
            <p v-if="isSaving">
              Uploading {{ fileCount }} files...
            </p>
        </div>
      </form>
      <!--SUCCESS-->
      <div v-if="isSuccess">
        <product-grid v-bind:response='response'></product-grid>
      </div>
      <!--FAILED-->
      <div v-if="isFailed">
        <product-grid v-bind:response='response'></product-grid>
      </div>
    </div>
  </div>
</template>

<script>
import { upload } from './file-upload.service'
import ProductGrid from '@/views/Grid.vue'

const STATUS_INITIAL = 0
const STATUS_SAVING = 1
const STATUS_SUCCESS = 2
const STATUS_FAILED = 3

export default {
  name: 'app',
  data () {
    return {
      uploadedFiles: [],
      uploadError: null,
      currentStatus: null,
      uploadFieldName: 'photos',
      response: []
    }
  },
  components: {
    ProductGrid
  },
  computed: {
    isInitial () {
      return this.currentStatus === STATUS_INITIAL
    },
    isSaving () {
      return this.currentStatus === STATUS_SAVING
    },
    isSuccess () {
      return this.currentStatus === STATUS_SUCCESS
    },
    isFailed () {
      return this.currentStatus === STATUS_FAILED
    }
  },
  methods: {
    reset () {
      // reset form to initial state
      this.currentStatus = STATUS_INITIAL
      this.uploadedFiles = []
      this.uploadError = null
    },
    save (formData) {
      // upload data to the server
      this.currentStatus = STATUS_SAVING

      upload(formData)
        .then(x => {
          console.log(x)
          this.response = JSON.parse(x)
          this.uploadedFiles = [].concat(x)
          this.currentStatus = STATUS_SUCCESS
        })
        .catch(err => {
          this.uploadError = err.response
          this.currentStatus = STATUS_FAILED
        })
    },
    filesChange (fieldName, fileList) {
      // handle file changes
      const formData = new FormData()

      if (!fileList.length) return

      // append the files to FormData
      Array
        .from(Array(fileList.length).keys())
        .map(x => {
          formData.append(fieldName, fileList[x], fileList[x].name)
          console.log(formData)
        })
        // save it
      this.save(formData)
    }
  },
  mounted () {
    this.reset()
  }
}

</script>

<style lang="scss">
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/base';
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/variables';
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/mixins';

@font-face {
  font-family: 'Avalon';
  src: url('../assets/fonts/Avalon-Book.eot');
  src: url('../assets/fonts/Avalon-Book.eot?#iefix') format('embedded-opentype'),
    url('../assets/fonts/Avalon-Book.woff2') format('woff2'),
    url('../assets/fonts/Avalon-Book.woff') format('woff'),
    url('../assets/fonts/Avalon-Book.ttf') format('truetype'),
    url('../assets/fonts/Avalon-Book.svg#Avalon-Book') format('svg');
  font-weight: 400;
  font-style: normal;
}

p {
  font-family: 'Avalon';
}

h1 {
  margin-top: 50px;
  margin-bottom: 50px;
}

.dropbox {
  border: 5px solid black;
  background: $brand-primary;
  color: $black;
  padding: 10px 10px;
  min-height: 200px; /* minimum height */
  position: relative;
  cursor: pointer;
}

.input-file {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 200px;
  position: absolute;
  cursor: pointer;
}

.dropbox p {
  font-size: 1.2em;
  text-align: center;
  padding: 50px 0;
}
</style>
