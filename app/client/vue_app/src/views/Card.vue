<template lang='pug'>
.col-6
  img.product-card-image(:src='product.variantImage')
  .product-card-heart
    p.product-card-brand(v-text='product.brandName')
    p.product-card-product(v-text='product.productName')
    p.product-price
      span.product-price-sale(v-text='"$"+ (product.variantPrice/100)')
</template>

<script>
export default {
  name: 'productCard',
  props: [
    'product'
  ]
}
</script>

<style lang="scss" scoped>
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/base';
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/variables';
@import '~sephora-style-guide/app/assets/stylesheets/sephora_style_guide/mixins';

.product-card-image {
  width: 100%;
}

.product-card-brand, .product-price-sale {
  font-weight: 600;
}

.col-6 {
  width: unset;
}
</style>
