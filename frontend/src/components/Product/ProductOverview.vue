<template>
  <div class="container text-center p-4">
    <h2 class="h1">
      {{ t('components.productOverview.title') }}
    </h2>
    <p class="fs-5 text-muted">
      {{ t('components.productOverview.subtitle') }}
    </p>
    <div class="form-switch d-flex justify-content-center align-items-center mb-4">
      <label
        class="form-check-label"
        :class="{'fw-bold': !monthlyInterval}"
        for="switchInterval"
      >
        {{ t('components.productOverview.yearlyPayment') }}
      </label>
      <input
        id="switchInterval"
        v-model="monthlyInterval"
        class="form-check-input mx-2"
        type="checkbox"
        role="switch"
      >
      <label
        class="form-check-label"
        :class="{'fw-bold': monthlyInterval}"
        for="switchInterval"
      >
        {{ t('components.productOverview.monthlyPayment') }}
      </label>
    </div>
    <div class="row row-cols-1 row-cols-md-3">
      <div
        v-for="product in products"
        :key="product"
        class="col"
      >
        <ProductCard
          :product="product"
          :interval="interval"
          @selection="(data) => {handleSelection(productId = data.productId, priceId = data.priceId)}"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import ProductCard from '@/components/Product/ProductCard'
import { useI18n } from 'vue-i18n'
import { useStore } from 'vuex'

// Enable access to localizations
const { t } = useI18n()
// Enable access to vuex store
const store = useStore()

const products = computed(() => {
  return store.getters['subscriptions/getProducts']
})

const monthlyInterval = ref(true)
const interval = computed(() => {
  return monthlyInterval.value ? 'month' : 'year'
})

function handleSelection (productId, priceId) {
  console.log(productId)
  console.log(priceId)
}

onMounted(() => {
  store.dispatch('subscriptions/retrieveProducts')
})
</script>
