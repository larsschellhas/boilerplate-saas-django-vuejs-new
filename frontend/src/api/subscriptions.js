import { api } from '@/api/axiosConfig'

function parsePotentialJSON (data) {
  try {
    return JSON.parse(data)
  } catch {
    return data
  }
}

export default {
  async getProducts () {
    try {
      const response = await api.get('products/')
      for (const product in response.data.results) {
        for (const metadataEntry in response.data.results[product].metadata) {
          response.data.results[product].metadata[metadataEntry] = parsePotentialJSON(response.data.results[product].metadata[metadataEntry])
        }
      }
      return { success: true, data: response.data }
    } catch (error) {
      return { success: false, errors: error }
    }
  }
}
