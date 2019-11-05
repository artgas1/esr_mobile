<template>
  <div>
    <div class="wrapper wrapper-full-page">
      <div
        class="full-page login-page section-image"
        filter-color="black"
        style="background: url(https://s3.amazonaws.com/uploads.bssskillmission/Jan122018160616.jpg) center / cover"
      >
        <!--   you can change the color of the filter page using: data-color="blue | purple | green | orange | red | rose " -->
        <div class="content">
          <div class="container">
            <div class="col-md-4 ml-auto mr-auto">
              <form @submit="doLogin">
                <div class="card card-login card-plain">
                  <div class="card-header">
                    <h2 class="text-white text-center">Вход</h2>
                  </div>
                  <div class="card-body">
                    <div class="input-group no-border form-control-lg">
                      <input
                        type="text"
                        class="form-control"
                        v-model="form.username"
                        placeholder="Логин"
                      />
                    </div>
                    <div class="input-group no-border form-control-lg">
                      <input
                        type="password"
                        v-model="form.password"
                        placeholder="Пароль"
                        class="form-control"
                      />
                    </div>
                    <button
                      type="submit"
                      class="mt-4 btn btn-primary btn-round btn-lg btn-block"
                    >Войти</button>
                  </div>
                  <div class="card-footer">
                    <div class="pull-left">
                      <h6>
                        <a href="#pablo" class="link footer-link">Регистрация</a>
                      </h6>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Auth from "../api/auth";
export default {
  name: "LoginPage",
  data() {
    return {
      form: {
        username: null,
        password: null
      }
    };
  },
  methods: {
    doLogin(event) {
      event.preventDefault();
      event.stopPropagation();
      Auth.tokenAuth(this.form)
        .then(
          response => (
            (localStorage.token = response.data.token),
            this.$router.push("/books/")
          )
        )
        .catch(window.console.warn);
    }
  }
};
</script>

<style>
</style>