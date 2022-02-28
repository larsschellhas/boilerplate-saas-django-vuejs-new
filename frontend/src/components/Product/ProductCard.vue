<template>
  <div
    :id="`product-card-${props.product.id}`"
    class="card product-card mb-4 rounded-3 shadow-sm text-center"
    :class="props.product.metadata.htmlClass"
  >
    <div class="card-header py-3">
      <h4 class="my-0 fw-normal">
        {{ props.product.name }}
      </h4>
    </div>
    <div class="card-body">
      <div class="card-title">
        <span class="h1">{{ formattedPrice }}</span><br>
        <span class="h4 text-muted fw-light">{{ t(formattedInterval) }}</span>
      </div>
      <ul class="product-features list-unstyled mt-3 mb-4">
        <li
          v-for="feature in props.product.metadata.featureList"
          :key="feature"
          class="product-feature"
        >
          {{ t(feature) }}
        </li>
      </ul>
      <button
        type="button"
        class="btn w-100 btn-lg"
        :class="props.product.metadata.buttonHtmlClass ? props.product.metadata.buttonHtmlClass : 'btn-primary'"
        @click="$emit('selection', {
          productId: props.product.id,
          priceId: price.id
        })"
      >
        {{ t(props.product.metadata.buttonText) }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useStore } from 'vuex'

const props = defineProps({
  product: {
    type: Object,
    default: () => {}
  },
  interval: {
    type: String,
    default: 'month'
  }
})

defineEmits(['selection'])

// Enable access to localizations
const { t } = useI18n()
// Enable access to vuex store
const store = useStore()

const price = computed(() => {
  return props.product.prices.find(price => price.recurring.interval === props.interval)
})

const formattedPrice = computed(() => {
  return (price.value.unit_amount / 100).toLocaleString(store.getters['localization/getLocale'], { style: 'currency', currency: price.value.currency, minimumFractionDigits: 2 })
})

const formattedInterval = computed(() => {
  const intervals = {
    year: 'components.productCard.intervals.year',
    month: 'components.productCard.intervals.month'
  }
  return intervals[price.value.recurring.interval]
})

</script>

<style lang="scss">
@import "@/styles/global";

.product-card.highlight {
  border-color: $primary;

  .card-header {
    background-color: $primary;
    color: #fff;
  }
}
</style>
