<template>
  <div
    v-if="profilePictureUrl !== '' && !deleted"
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

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

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
    },
    deleted: {
      type: Boolean,
      default: false
    }
  },
  setup (props) {
    // Enable access to vuex store
    const store = useStore()

    const profilePictureUrl = computed(() => {
      if (props.imgUrl !== '') {
        return props.imgUrl
      } else {
        return store.getters['user/getProfilePicture']
      }
    })
    return { profilePictureUrl }
  }
}
</script>
