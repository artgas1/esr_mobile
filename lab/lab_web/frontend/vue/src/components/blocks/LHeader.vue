<template>
  <!-- Navbar -->
  <div>
    <nav class="navbar navbar-expand-lg navbar-transparent bg-primary navbar-absolute">
      <div class="container-fluid">
        <div class="navbar-wrapper">
          <div class="navbar-toggle">
            <button type="button" class="navbar-toggler">
              <span class="navbar-toggler-bar bar1"></span>
              <span class="navbar-toggler-bar bar2"></span>
              <span class="navbar-toggler-bar bar3"></span>
            </button>
          </div>
          <a class="navbar-brand" href="#pablo">{{ title }}</a>
        </div>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navigation"
          aria-controls="navigation-index"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-bar navbar-kebab"></span>
          <span class="navbar-toggler-bar navbar-kebab"></span>
          <span class="navbar-toggler-bar navbar-kebab"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navigation">
          <form>
            <div class="input-group no-border">
              <input type="text" value class="form-control" placeholder="Поиск..." />
              <div class="input-group-append">
                <div class="input-group-text">
                  <i class="jam jam-search"></i>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </nav>
    <!-- End Navbar -->
    <div class="panel-header panel-header-md">
      <div class="container-fluid">
        <div class="container-fluid">
          <div class="d-flex align-items-center">
            <h2 class="text-white font-weight-100">{{ title }}</h2>
            <button v-for="button in buttons" v-bind:key="button.text" class="btn btn-primary ml-auto shadow-sm font-weight-bold text-uppercase text-decoration-none" @click="button.click">
                {{ button.text }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "LHeader",
    props: {
        title: {
            type: String
        }, 
        buttons: {
            type: Array, 
            default: () => []
        }
    }
};
</script>

<style>
</style>