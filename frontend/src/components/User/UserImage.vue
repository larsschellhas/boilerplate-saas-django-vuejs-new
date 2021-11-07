<template>
  <img
    v-if="imgUrl"
    class="rounded-circle"
    :src="imgUrl"
    :height="size"
    :width="size"
  >
  <i
    v-else
    class="fas fa-user-circle"
    style="font-size: 32px; width: 32px;"
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
