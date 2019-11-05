<template>
  <div class="table-responsive">
    <table class="table table-shopping" style="table-layout: auto;">
      <thead class="text-primary font-weight-bold">
        <tr>
          <th v-for="column in columns" v-bind:key="column" style="max-width: 12.5%;">
            <p class="font-weight-bold">{{column}}</p>
          </th>
        </tr>
      </thead>
      <tbody>
        <slot></slot>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "LTable", 
  props: {
    columns: {
      type: Array, 
      default: () => []
    }
  }
};
</script>

<style>
</style>