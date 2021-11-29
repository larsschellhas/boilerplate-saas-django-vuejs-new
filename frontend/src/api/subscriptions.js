import { api } from '@/api/axiosConfig'

export default {
  async getProducts () {
    try {
      const response = await api.get('products/')
      for (const product in response.data.results) {
        for (const metadataEntry in response.data.results[product].metadata) {
          response.data.results[product].metadata[metadataEntry] = JSON.parse(response.data.results[product].metadata[metadataEntry])
        }
      }
      return { success: true, data: response.data }
    } catch (error) {
      return { success: false, errors: error }
    }
  }
}
