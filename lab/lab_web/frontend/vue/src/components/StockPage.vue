<template>
  <div id="wrapper">
    <l-nav current-menu-item="stock"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Склад" :buttons="buttons" />
      <div class="content">
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-body">
                <l-table
                  v-if="materials.length"
                  :columns="['ID','Наименование', 'Единица измерения', 'Доступно', 'Лимит', 'Комментарий', 'Действия']"
                >
                  <tr v-for="material in materials" v-bind:key="material.id">
                    <td>{{material.id}}</td>
                    <td>{{material.name}}</td>
                    <td>1 {{material.unit}}</td>
                    <td>?</td>
                    <td>{{material.limit}} {{material.unit}}</td>
                    <td>{{material.comment}}</td>
                    <td>
                      <h5>
                        <a href="#">
                          <i class="jam jam-pencil"></i>
                        </a>
                        <a
                          href="#"
                          class="zub-release-material"
                        >
                          <i class="jam jam-cutter text-danger"></i>
                        </a>
                        <a href="#">
                          <i class="jam jam-trash text-danger"></i>
                        </a>
                      </h5>
                    </td>
                  </tr>
                </l-table>
                <div class="text-center text-muted p-4" v-if="!materials.length">
                  Нет материалов
                  <br />
                  <br />Добавьте материал, используя кнопку "Добавить"
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
import Materials from "../api/materials";

export default {
  name: "StockPage",
  components: {
    LNav,
    LHeader,
    LTable, 
    LFooter
  },
  data() {
    return {
      buttons: [
        {
          text: "Добавить материал",
          click: event => {
            event.preventDefault();
            this.$router.push("/materials/add/");
            return false;
          }
        }
      ],
      materials: []
    };
  },
  created() {
    Materials.get({}).then(response => (this.materials = response.data));
  }
};
</script>

<style>
</style>