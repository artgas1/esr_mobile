<template>
  <div id="wrapper">
    <l-nav current-menu-item="books"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Добавить клинику" :buttons="buttons" />
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
                  v-model="clinic.clinic_name"
                />
                <input
                  type="text"
                  class="form-control mb-4"
                  placeholder="Контакты"
                  v-model="clinic.contacts"
                />
                <textarea class="form-control" placeholder="Комментарий" v-model="clinic.comment" />
              </div>
            </div>
          </div>
          <div class="col-12 col-md-6 col-lg-4">
            <div class="card">
              <div class="card-header">
                <h5>Прайс-лист</h5>
              </div>
              <div class="card-body">
                <l-list
                  :single="true"
                  no-items-text="Прайс-лист не выбран"
                  add-item-text="Выбрать прайс-лист"
                  add-item-input-placeholder="Название прайс-листа"
                  :suggested-items-filter="suggestedItemsFilter"
                  ref="itemsList"
                  @change="item => this.clinic.price_list = item ? item.id : 0"
                > 
                  <template v-slot:itemRow="{ item }">
                    <p class="my-0">{{item.price_list_name}}</p>
                  </template>
                  <template v-slot:addItemRow="{ item }">
                    <p class="my-0">{{item.price_list_name}}</p>
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
import Clinics from "../api/clinics";
import Pricelists from "../api/pricelists";
export default {
  name: "AddClinicPage",
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
            Clinics.create(this.clinic).then(() =>
              this.$router.push("/books/clinics/")
            );
          }
        }
      ],
      clinic: {
        clinic_name: null,
        contacts: null,
        comment: null,
        price_list: 0
      }
    };
  }, 
  methods: {
    suggestedItemsFilter(item, query){
      return item.price_list_name.indexOf(query) + 1;
    }
  }, 
  created(){
    Pricelists.Works.get().then(response => {
      this.$refs.itemsList.$emit("all-items-available", response.data);
    })
  }
};
</script>

<style>
</style>