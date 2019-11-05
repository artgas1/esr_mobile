<template>
  <div id="wrapper">
    <l-nav current-menu-item="books"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header :title="title" :buttons="buttons" />
      <div class="content">
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-body">
                <l-table v-if="items.length" :columns="['ID','Наименование', 'Действия']">
                  <tr v-for="item in items" v-bind:key="item.id">
                    <td>{{item.id}}</td>
                    <td>{{item.price_list_name}}</td>
                    <td>
                      <h5>
                        <a href="#">
                          <i class="jam jam-pencil"></i>
                        </a>
                        <a href="#" class="zub-release-material">
                          <i class="jam jam-cutter text-danger"></i>
                        </a>
                        <a href="#">
                          <i class="jam jam-trash text-danger"></i>
                        </a>
                      </h5>
                    </td>
                  </tr>
                </l-table>
                <div class="text-center text-muted p-4" v-if="!items.length">
                  Нет прайс-листов
                  <br />
                  <br />Добавьте прайс-лист, используя кнопку "Добавить"
                </div>
              </div>
            </div>
          </div>
          <l-footer />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LNav from "./blocks/LNav";
import LHeader from "./blocks/LHeader";
import LTable from "./blocks/LTable";
import LFooter from "./blocks/LFooter";
import Pricelists from "../api/pricelists";
export default {
  name: "PricelistsBookPage",
  components: {
    LNav,
    LHeader,
    LTable,
    LFooter
  },
  computed: {
    pricelistType() {
      return this.$route.params.type;
    }, 
    title(){
      let title = "Справочники - Прайс-листы - ";
      if(this.pricelistType === "works"){
        title += "Работы";
      }else{
        title += "Операции"
      }
      return title;
    }
  },
  data() {
    return {
      items: [],
      buttons: [
        {
          text: "Добавить прайс-лист",
          click: () => this.$router.push(`/pricelists/${this.pricelistType}/add/`)
        }
      ]
    };
  },
  created() {
    let handleResponse = response => {
      this.items = response.data;
    };
    if (this.pricelistType === "works") {
      Pricelists.Works.get().then(handleResponse);
    } else {
      Pricelists.Operations.get().then(handleResponse);
    }
  }
};
</script>

<style>
</style>