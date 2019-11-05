<template>
  <div id="wrapper">
    <l-nav current-menu-item="books"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Добавить прайс-лист" :buttons="buttons" />
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
                  v-model="pricelist.price_list_name"
                />
              </div>
            </div>
          </div>
          <div class="col-12 col-md-6 col-lg-4">
            <div class="card">
              <div class="card-header">
                <h5>{{itemsTitle}}</h5>
              </div>
              <div class="card-body">
                <l-list
                  :items="items"
                  :no-items-text="noItemsText"
                  :add-item-text="addItemText"
                  :add-item-input-placeholder="addItemInputPlaceholder"
                  :suggested-items-filter="suggestedItemsFilter"
                  :unique="true"
                  :unique-items-filter="uniqueItemsFilter"
                  ref="itemsList"
                  @change="items => this.items = items"
                >
                  <template v-slot:itemRow="{ item }">
                    <div class="d-flex align-items-center">
                      <div>
                        <p
                          class="my-0"
                          v-if="pricelistType === 'operations'"
                        >{{item.operation_name}}</p>
                        <p class="my-0" v-if="pricelistType === 'works'">{{item.work_name}}</p>
                      </div>
                      <div class="ml-auto mr-4">
                        <div class="input-group">
                          <input
                            class="form-control"
                            type="number"
                            :value="1"
                            :min="1"
                            @input="item.price = parseInt($event.target.value)"
                          />
                          <div class="input-group-append">
                            <span class="input-group-text">&#x20bd;</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </template>
                  <template v-slot:addItemRow="{ item }">
                    <p class="my-0" v-if="pricelistType === 'operations'">{{item.operation_name}}</p>
                    <p class="my-0" v-if="pricelistType === 'works'">{{item.work_name}}</p>
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
import Pricelists from "../api/pricelists";
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
            let redirectOnSuccess = () =>
              this.$router.push(`/books/pricelists/${this.pricelistType}/`);
            if (this.pricelistType === "works") {
              Pricelists.Works.create(this.pricelist).then(response => {
                let id = response.data.id;
                Works.Prices.create(
                  this.items.map(item => ({
                    work: item.id,
                    price: item.price,
                    price_list: id
                  }))
                ).then(redirectOnSuccess);
              });
            } else {
              Pricelists.Operations.create(this.pricelist).then(response => {
                let id = response.data.id;
                Operations.Prices.create(
                  this.items.map(item => ({
                    operation: item.id,
                    price: item.price,
                    price_list: id
                  }))
                ).then(redirectOnSuccess);
              });
            }
          }
        }
      ],
      pricelist: {
        price_list_name: null
      },
      items: []
    };
  },
  computed: {
    pricelistType() {
      return this.$route.params.type;
    },
    noItemsText() {
      if (this.pricelistType === "works") {
        return "Нет работ";
      }
      return "Нет операций";
    },
    addItemText() {
      if (this.pricelistType === "works") {
        return "Добавить работу";
      }
      return "Добавить операцию";
    },
    addItemInputPlaceholder() {
      if (this.pricelistType === "works") {
        return "Название работы";
      }
      return "Название операции";
    },
    itemsTitle() {
      if (this.pricelistType === "works") {
        return "Работы";
      }
      return "Операции";
    }
  },
  created() {
    let handleResponse = response => {
      let items = response.data.map(item => Object.assign(item, { price: 1 }));
      this.$refs.itemsList.$emit("all-items-available", items);
    };
    if (this.pricelistType === "works") {
      Works.get().then(handleResponse);
    } else {
      Operations.get().then(handleResponse);
    }
  },
  methods: {
    suggestedItemsFilter(item, query) {
      if (this.pricelistType === "works") {
        return item.work_name.indexOf(query) + 1;
      }
      return item.operation_name.indexOf(query) + 1;
    },
    uniqueItemsFilter(item, alreadySelected) {
      for (let i = 0; i < alreadySelected.length; ++i) {
        if (alreadySelected[i].id === item.id) {
          return false;
        }
      }
      return true;
    }
  }
};
</script>

<style>
</style>