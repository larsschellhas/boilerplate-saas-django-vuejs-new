<template>
  <div
    class="dashboard d-flex justify-content-center m-4"
  >
    <h2>{{ title }}</h2>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'Dashboard',
  setup () {
    const store = useStore()

    const title = computed(() => {
      return `Hello ${store.getters['user/getFirstName']} ${store.getters['user/getLastName']}! Great day for fishin', ain't it?`
    })

    return { title }
  }
}
</script>
