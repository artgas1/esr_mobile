<template>
  <div id="wrapper">
    <l-nav current-menu-item="books"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Добавить операцию" :buttons="buttons" />
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
                  v-model="operation.operation_name"
                />
              </div>
            </div>
          </div>
          <div class="col-12 col-md-6 col-lg-4">
            <div class="card">
              <div class="card-header">
                <h5>Материалы</h5>
              </div>
              <div class="card-body">
                <l-list
                  add-item-text="Добавить материал"
                  no-items-text="Нет материалов"
                  ref="materialsList"
                  :suggested-items-filter="suggestedItemsFilter"
                  @change="items => this.operation.materials = items"
                >
                  <template v-slot:itemRow="{ item }">
                    <div class="d-flex align-items-center">
                      <div>
                        <p class="my-0">{{item.material_name}}</p>
                      </div>
                      <div class="ml-auto mr-4">
                        <div class="input-group">
                          <input
                            class="form-control"
                            type="number"
                            :value="0"
                            :min="0"
                            :max="item.limit"
                            @input="item.amount = parseInt($event.target.value)"
                          />
                          <div class="input-group-append">
                            <span class="input-group-text">{{item.unit}}</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </template>
                  <template v-slot:addItemRow="{ item }">
                    <p class="my-0">{{item.material_name}}</p>
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
import Operations from "../api/operations";
import Materials from "../api/materials";
export default {
  name: "AddOperationPage",
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
            Operations.create(this.operation).then(
              response => {
                let operation = response.data,
                  materials = this.operation.materials.map(item => ({
                    operation: operation.id,
                    material: item.id,
                    amount: item.amount
                  }));
                Materials.UsedOnOperation.create(materials).then(() =>
                  this.$router.push("/books/operations/")
                );
              }
            );
          }
        }
      ],
      operation: {
        operation_name: null,
        materials: []
      }
    };
  },
  created() {
    Materials.get().then(response => {
      let items = response.data.map(x => Object.assign(x, { amount: 0 }));
      this.$refs.materialsList.$emit("all-items-available", items);
    });
  },
  methods: {
    suggestedItemsFilter(item, query) {
      return item.material_name.indexOf(query) + 1;
    }
  }
};
</script>

<style>
</style>