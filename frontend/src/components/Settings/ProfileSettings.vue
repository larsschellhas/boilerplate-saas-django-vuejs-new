<template>
  <SettingsSubPage
    id="profile-settings"
    title="components.profileSettings.title"
  >
    <template #header-button>
      <button
        type="submit"
        class="btn btn-success text-light"
        @click.prevent="handleSave"
      >
        <div
          v-if="loading"
          class="spinner-border spinner-border-sm"
          role="status"
        >
          <span class="visually-hidden">{{ t("forms.loading") }}</span>
        </div>
        <span v-else>
          {{ t("forms.save") }}
        </span>
      </button>
    </template>
    <template #default>
      <SettingsSubPageSection
        anchor="profile-picture"
        title="components.profileSettings.profilePicture.title"
      >
        <div class="row d-flex align-items-center justify-content-center">
          <div class="col-12 col-md-6 d-flex align-items-center justify-content-center">
            <UserImage :size="160" />
          </div>
          <div class="col-12 col-md-6 d-flex flex-column justify-content-center">
            <label
              for="profile-picture-input"
              class="form-label mt-2"
            >
              {{ t("components.profileSettings.profilePicture.new-profile-picture") }}
            </label>
            <input
              id="profile-picture-input"
              ref="profilePictureInput"
              class="form-control"
              type="file"
              accept="image/*"
              @change="handleFileSelection( $event )"
            >
          </div>
        </div>
      </SettingsSubPageSection>
      <SettingsSubPageSection
        anchor="profile-name"
        title="components.profileSettings.name.title"
      >
        <div class="row">
          <div class="col-12 col-md-6">
            <label
              for="firstname"
              class="form-label mt-2"
            >
              {{ t("forms.firstname") }}
            </label>
            <input
              id="firstname"
              v-model="profileData.firstname"
              class="form-control"
              :class="{
                'is-invalid': errors.firstname && validated,
                'is-valid': !errors.firstname && validated,
              }"
            >
            <div
              v-if="errors.firstname"
              class="invalid-feedback"
            >
              <span
                v-for="(error, index) in errors.firstname"
                :key="index"
              >
                {{ error }}&nbsp;</span>
            </div>
          </div>
          <div class="col-12 col-md-6">
            <label
              for="lastname"
              class="form-label mt-2"
            >
              {{ t("forms.lastname") }}
            </label>
            <input
              id="lastname"
              v-model="profileData.lastname"
              class="form-control"
              :class="{
                'is-invalid': errors.lastname && validated,
                'is-valid': !errors.lastname && validated,
              }"
            >
            <div
              v-if="errors.lastname"
              class="invalid-feedback"
            >
              <span
                v-for="(error, index) in errors.lastname"
                :key="index"
              >
                {{ error }}&nbsp;</span>
            </div>
          </div>
        </div>
      </SettingsSubPageSection>
      <SettingsSubPageSection
        anchor="profile-email"
        title="components.profileSettings.email.title"
      >
        <label
          for="username"
          class="form-label mt-2"
        >
          {{ t("forms.email") }}
        </label>
        <input
          v-model="profileData.username"
          type="email"
          class="form-control"
          :class="{
            'is-invalid': errors.username && validated,
            'is-valid': !errors.username && validated,
          }"
        >
        <div
          v-if="errors.username"
          class="invalid-feedback"
        >
          <span
            v-for="(error, index) in errors.username"
            :key="index"
          >
            {{ error }}&nbsp;</span>
        </div>
      </SettingsSubPageSection>
      <SettingsSubPageSection
        anchor="profile-password"
        title="components.profileSettings.password.title"
      >
        <label
          for="password"
          class="form-label mt-2"
        >
          {{ t("forms.password") }}
        </label>
        <input
          v-model="profileData.password"
          type="password"
          class="form-control"
          :class="{
            'is-invalid': errors.password && validated,
            'is-valid': !errors.password && validated,
          }"
        >
        <div
          v-if="errors.password"
          class="invalid-feedback"
        >
          <span
            v-for="(error, index) in errors.password"
            :key="index"
          >
            {{ error }}&nbsp;</span>
        </div>
      </SettingsSubPageSection>
    </template>
  </SettingsSubPage>
</template>

<script>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useStore } from 'vuex'
import SettingsSubPage from '@/components/Settings/SettingsSubPage'
import SettingsSubPageSection from '@/components/Settings/SettingsSubPageSection'
import UserImage from '@/components/User/UserImage'

export default {
  name: 'ProfileSettings',
  components: {
    SettingsSubPage,
    SettingsSubPageSection,
    UserImage
  },
  setup () {
    // Enable access to localizations
    const { t } = useI18n()
    // Enable access to vuex store
    const store = useStore()

    const loading = ref(false)

    const errors = ref({
      username: '',
      password: '',
      firstname: '',
      lastname: '',
      profilePicture: ''
    })

    const validated = ref(false)

    const getDefaultProfileData = () => {
      return {
        username: store.getters['user/getEmail'],
        password: '',
        firstname: store.getters['user/getFirstname'],
        lastname: store.getters['user/getLastname'],
        profilePicture: ''
      }
    }
    const profileData = ref(getDefaultProfileData())
    const profilePictureInput = ref(null)

    function handleFileSelection (event) {
      profileData.value.profilePicture = event.target.files[0]
    }

    async function handleSave () {
      loading.value = true
      if (profileData.value.profilePicture !== '') {
        store.dispatch({
          type: 'user/updateProfilePicture',
          profilePicture: profileData.value.profilePicture
        })
          .then((results) => {
            if (!results.success) {
              for (const key in results.errors) {
                errors.value[key] = results.errors[key]
              }
            } else {
              profilePictureInput.value.value = null
            }
          })
      }
      store.dispatch({
        type: 'user/updateProfileData',
        username: profileData.value.username,
        password: profileData.value.password,
        firstname: profileData.value.firstname,
        lastname: profileData.value.lastname
      })
        .then((results) => {
          if (!results.success) {
            for (const key in results.errors) {
              errors.value[key] = results.errors[key]
            }
          } else {
            profileData.value = getDefaultProfileData()
            profilePictureInput.value.value = null
          }
          validated.value = true
          loading.value = false
        })
    }

    return { t, errors, validated, profileData, profilePictureInput, loading, handleFileSelection, handleSave, store }
  }
}
</script>
