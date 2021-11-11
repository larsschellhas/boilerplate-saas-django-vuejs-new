<template>
  <div class="user-banner d-flex p-2 my-2">
    <UserImage
      :size="imageSize"
      class="me-2 text-primary text-opacity-50"
    />
    <div class="user-details d-flex flex-column justify-center">
      <div class="user-name">
        {{ user.fullName }}
      </div>
      <div class="user-email">
        {{ user.email }}
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useStore } from 'vuex'
import UserImage from '@/components/User/UserImage'

export default {
  components: {
    UserImage
  },
  props: {
    imageSize: {
      type: Number,
      default: 48
    }
  },
  setup (props) {
    // Enable access to localizations
    const { t } = useI18n()
    // Enable access to vuex store
    const store = useStore()

    const user = computed(() => {
      return {
        fullName: store.getters['user/getFullName'],
        email: store.getters['user/getEmail'],
        isLoggedIn: store.getters['user/isLoggedIn']
      }
    })
    return { t, user }
  }
}
</script>

<style lang="scss">
.user-banner {
  .user-details {
    .user-name {
      font-weight: bold;
    }

    .user-email {
      font-size: 0.8em;
    }
  }
}
</style>
