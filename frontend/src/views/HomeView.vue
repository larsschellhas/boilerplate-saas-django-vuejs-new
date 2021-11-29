<template>
  <div
    id="home-view"
    class="d-flex flex-column align-items-center"
  >
    <div class="container-fluid text-center bg-primary text-white p-4">
      <h2>{{ t("views.home.title") }}</h2>
    </div>
    <ProductOverview />
  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import ProductOverview from '@/components/Product/ProductOverview'

// Enable access to localizations
const { t } = useI18n()
</script>
