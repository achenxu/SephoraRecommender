import * as axios from 'axios'

const BASE_URL = 'http://localhost:5000'

function upload (formData) {
  const url = `${BASE_URL}/api/upload`
  return axios.post(url, formData)
  // get data
    .then(x => x.data)
}

export { upload }
