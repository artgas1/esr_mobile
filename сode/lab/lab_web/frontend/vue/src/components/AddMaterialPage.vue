<template>
  <div id="wrapper">
    <l-nav current-menu-item="books"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Добавить материал" :buttons="buttons" />
      <div class="content">
        <div class="row">
          <div class="col-12 col-md-6 col-lg-4">
            <div class="card">
              
              <div class="card-body">
                <input
                  type="text"
                  class="form-control mb-4"
                  placeholder="Название"
                  v-model="material.material_name"
                />
                <label for="material-unit-select">Единица измерения</label>
                <select class="form-control mb-4" id="material-unit-selec" v-model="material.unit">
                  <option value="gr">Грамм</option>
                  <option value="sht">Штука</option>
                </select>
                <input
                  type="number"
                  class="form-control mb-4"
                  placeholder="Максимальное количество"
                  v-model="material.limit"
                />
                <textarea
                  class="form-control"
                  placeholder="Комментарий"
                  v-model="material.comment"
                />
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
import Materials from '../api/materials';
export default {
  name: "AddMaterialPage",
  components: {
    LNav,
    LHeader
  },
  data() {
    return {
      buttons: [
        {
          text: "Сохранить",
          click: () => {
            Materials.create(this.material).then(() => this.$router.push('/books/materials/'));
          }
        }
      ],
      material: {
        material_name: null,
        unit: null,
        limit: null,
        comment: null
      }
    };
  }
};
</script>

<style>
</style>