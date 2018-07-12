<template lang='pug'>
#products-grid
  .row
    .col-3.product-item(v-for='product in response')
      product-card(:product='product')
</template>

<script>
import ProductCard from '@/views/Card.vue'

export default {
  name: 'prodGrid',
  components: {
    ProductCard
  },
  props: [
    'response'
  ]
}
</script>

<style lang="scss">
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/base';
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/variables';
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/mixins';

.row {
  display: flex;
  align-content: center;
}
</style>
