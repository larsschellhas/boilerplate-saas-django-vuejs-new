<template>
  <img
    v-if="imgUrl"
    class="rounded-circle user-image"
    :src="imgUrl"
    :height="size"
    :width="size"
  >
  <i
    v-else
    class="fas fa-user-circle user-image"
    :style="`font-size: ${size}px; width: ${size}px;`"
  />
</template>

<script>
export default {
  name: 'UserImage',
  props: {
    imgUrl: {
      type: String,
      default: ''
    },
    size: {
      type: Number,
      default: 32
    }
  },
  setup (props) {
    return {}
  }
}
</script>
