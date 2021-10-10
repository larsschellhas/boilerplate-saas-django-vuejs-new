<template>
  <div class="auth-form px-3 mt-4 d-flex flex-column align-items-center">
    <p class="fs-4 text fw-light">
      Sign in to {{ pagetitle }}
    </p>
    <div class="card bg-light shadow rounded mb-4 w-100">
      <div class="card-body">
        <form>
          <div class="mb-3">
            <label
              for="email1"
              class="form-label"
            >Email address</label>
            <input
              id="email1"
              type="email"
              class="form-control"
              aria-describedby="emailHelp"
            >
            <div
              id="emailHelp"
              class="form-text"
            />
          </div>
          <div class="mb-3">
            <label
              for="password1"
              class="form-label"
            >Password</label>
            <input
              id="password1"
              type="password"
              class="form-control"
            >
          </div>
          <button
            type="submit"
            class="btn btn-success w-100"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
    <div class="card w-100">
      <div class="card-body text-center">
        New to {{ pagetitle }}? <router-link to="/register">
          Create an account.
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    pagetitle: {
      type: String,
      default: 'SimplySaaS'
    }
  }
}

</script>

<style>
.auth-form {
  width: 350px;
  margin: 0 auto;
}
</style>
