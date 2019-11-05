<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
let currentUserChanges = 0;
export default {
  name: 'app',
  data(){
    return {
      currentUser: null
    }
  },
  watch: {
    currentUser(){
      if(currentUserChanges > 1){
        window.location.reload();
      }
      currentUserChanges++;
    }
  },
  created(){
    this.currentUser = Object.assign(this.currentUser || {}, {"id": 1});
    this.currentUser = Object.assign(this.currentUser || {}, {"id": 2});
  }
}
</script>