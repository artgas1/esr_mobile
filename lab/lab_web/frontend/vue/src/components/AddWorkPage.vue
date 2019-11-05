<template>
  <div id="wrapper">
    <l-nav current-menu-item="books"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Добавить работу" :buttons="buttons" />
      <div class="content">
        <div class="row">
          <div class="col-12 col-md-6 col-lg-4">
            <div class="card">
              <div class="card-header">
                <h5>Общая информация</h5>
              </div>
              <div class="card-body">
                <input
                  type="text"
                  class="form-control mb-4"
                  placeholder="Название"
                  v-model="work.work_name"
                />
              </div>
            </div>
          </div>
          <div class="col-12 col-md-6 col-lg-4">
            <div class="card">
              <div class="card-header">
                <h5>Операции</h5>
              </div>
              <div class="card-body">
                <l-list
                  :items="work.operations"
                  no-items-text="Нет операций"
                  add-item-text="Добавить операцию"
                  add-item-input-placeholder="Название операции"
                  :suggested-items-filter="suggestedItemsFilter"
                  ref="operationsList"
                  @change="items => this.work.operations = items"
                >
                  <template v-slot:itemRow="{ item }">
                    <p class="my-0">{{item.operation_name}}</p>
                  </template>
                  <template v-slot:addItemRow="{ item }">
                    <p class="my-0">{{item.operation_name}}</p>
                  </template>
                </l-list>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LNav from "./blocks/LNav";
import LHeader from "./blocks/LHeader";
import LList from "./blocks/LList";
import Works from "../api/works";
import Operations from "../api/operations";
export default {
  name: "AddWorkPage",
  components: {
    LNav,
    LHeader,
    LList
  },
  data() {
    return {
      buttons: [
        {
          text: "Сохранить",
          click: () => {
            Works.create(
              Object.assign({}, this.work, {
                operations: this.work.operations.map(t => t.id)
              })
            ).then(() => this.$router.push("/books/works/"));
          }
        }
      ],
      work: {
        work_name: null,
        operations: []
      }
    };
  },
  created() {
    Operations.get().then(response => {
      this.$refs.operationsList.$emit("all-items-available", response.data);
    });
  },
  methods: {
    suggestedItemsFilter(item, query) {
      return item.operation_name.indexOf(query) + 1;
    }
  }
};
</script>

<style>
</style>