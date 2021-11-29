import subscriptions from '@/api/subscriptions'

const getDefaultState = () => {
  return {
    products: []
  }
}

const state = getDefaultState()

const getters = {
  getProducts (state) {
    return state.products
  }
}

const actions = {
  async retrieveProducts ({ commit, getters }) {
    const result = await subscriptions.getProducts()
    if ('position' in result.data.results[0].metadata) {
      result.data.results.sort((a, b) => (a.metadata.position > b.metadata.position ? 1 : -1))
    }
    if (result.success) {
      commit('updateProducts', result.data.results)
      return { success: true }
    } else {
      return result
    }
  }
}

const mutations = {
  updateProducts (state, status) {
    state.products = status
  },
  resetState (state) {
    Object.assign(state, getDefaultState())
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
