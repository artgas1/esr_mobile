<template>
  <div id="wrapper">
    <l-nav current-menu-item="books"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Справочники - Клиники" :buttons="buttons" />
      <div class="content">
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-body">
                  <l-table
                  v-if="items.length"
                  :columns="['ID','Название', 'Контакты', 'Комментарий', 'Действия']"
                >
                  <tr v-for="item in items" v-bind:key="item.id">
                    <td>{{item.id}}</td>
                    <td>{{item.name}}</td>
                    <td>{{item.contacts}}</td>
                    <td>{{item.comment}}</td>
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
                  Нет клиник
                  <br />
                  <br />Добавьте клинику, используя кнопку "Добавить"
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
import LFooter from "./blocks/LFooter";
import LTable from "./blocks/LTable";
import Clinics from "../api/clinics";
export default {
  name: "ClinicsBookPage",
  components: {
      LNav, 
      LHeader, 
      LTable, 
      LFooter
  },
  data() {
    return {
      items: [],
      buttons: [
        {
          text: "Добавить клинику",
          click: () => this.$router.push("/clinics/add/")
        }
      ]
    };
  },
  created() {
    Clinics.get({}).then(response => (this.items = response.data));
  }
};
</script>

<style>
</style>