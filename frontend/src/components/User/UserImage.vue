<template>
  <div
    v-if="profilePictureUrl && !deleted"
    class="rounded-circle user-image"
    :style="`height: ${size}px; width: ${size}px; background-image: url( ${profilePictureUrl} ); background-size: cover; background-position: center;`"
  />
  <div
    v-else
    class="rounded-circle user-image"
    :style="`height: ${size}px; width: ${size}px;`"
  >
    <i
      class="fas fa-user-circle"
      :style="`font-size: ${size}px; width: ${size}px;`"
    />
  </div>
</template>

<script setup>
import { computed, defineProps } from 'vue'
import { injectAuth } from 'vue-auth0-plugin'

const props = defineProps({
  imgUrl: {
    type: String,
    default: ''
  },
  size: {
    type: Number,
    default: 32
  },
  deleted: {
    type: Boolean,
    default: false
  }
})

const auth = injectAuth()

const profilePictureUrl = computed(() => {
  if (props.imgUrl !== '') {
    return props.imgUrl
  } else if (auth.user) {
    return auth.user.picture
  } else {
    return ''
  }
})

</script>
