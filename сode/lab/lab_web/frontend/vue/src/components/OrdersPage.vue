<template>
  <div id="wrapper">
    <l-nav current-menu-item="orders"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Наряды" :buttons="buttons" />
      <div class="content">
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-shopping" style="table-layout: auto;">
                    <thead class="text-primary font-weight-bold">
                      <th style="max-width: 12.5%;">
                        <p class="font-weight-bold">ID</p>
                      </th>
                      <th style="max-width: 12.5%;">
                        <p class="font-weight-bold">Пациент</p>
                      </th>
                      <th style="max-width: 12.5%;">
                        <p class="font-weight-bold">Клиника</p>
                      </th>
                      <th style="max-width: 12.5%;">
                        <p class="font-weight-bold">Врач</p>
                      </th>
                      <th style="max-width: 12.5%;">
                        <p class="font-weight-bold">Срок выполнения</p>
                      </th>
                      <th style="max-width: 12.5%;">
                        <p class="font-weight-bold">Прогресс выполнения</p>
                      </th>
                      <th style="width: 20%;">
                        <p class="font-weight-bold">Комментарий</p>
                      </th>
                      <th style="max-width: 12.5%;">
                        <p class="font-weight-bold">Действия</p>
                      </th>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="col">4</th>
                        <td>Иванов Иван Иванович</td>
                        <td>ООО "Зе бест зубная клиника"</td>
                        <td>Петров Петр Петрович</td>
                        <td>20.09.2019</td>
                        <td>
                          <span class="zub-order-progress bg-warning mr-2"></span>Частично выполнен
                        </td>
                        <td>-</td>
                        <td>
                          <h5>
                            <a href="#">
                              <i class="jam jam-pencil"></i>
                            </a>
                            <a href="#">
                              <i class="jam jam-trash text-danger"></i>
                            </a>
                          </h5>
                        </td>
                      </tr>
                      <tr>
                        <th scope="col">7</th>
                        <td>Иванов Иван Иванович</td>
                        <td>ООО "Зе бест зубная клиника"</td>
                        <td>Петров Петр Петрович</td>
                        <td>20.09.2019</td>
                        <td>
                          <span class="zub-order-progress bg-warning mr-2"></span>Частично выполнен
                        </td>
                        <td>-</td>
                        <td>
                          <h5>
                            <a href="#">
                              <i class="jam jam-pencil"></i>
                            </a>
                            <a href="#">
                              <i class="jam jam-trash text-danger"></i>
                            </a>
                          </h5>
                        </td>
                      </tr>
                      <tr>
                        <th scope="col">10</th>
                        <td>Иванов Иван Иванович</td>
                        <td>ООО "Зе бест зубная клиника"</td>
                        <td>Петров Петр Петрович</td>
                        <td>20.09.2019</td>
                        <td>
                          <span class="zub-order-progress bg-warning mr-2"></span>Частично выполнен
                        </td>
                        <td>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat beatae distinctio, ab vero quos cum unde. Rem eligendi quos nesciunt natus doloribus, repudiandae, qui reprehenderit laudantium ratione accusamus labore perferendis est, voluptatum, deserunt veniam consectetur non vel quasi fugit. Nostrum quo magnam molestias veniam eum nisi accusantium eaque sequi, praesentium aliquam nam, quisquam assumenda numquam laudantium voluptatem, optio officiis atque culpa tempora, ad. Esse voluptates minima repudiandae exercitationem ipsam ut deleniti eveniet, in nesciunt voluptatibus quo repellendus eius itaque sit voluptas laboriosam distinctio delectus alias, aspernatur. Error dicta natus laborum minima, modi velit ex. Saepe blanditiis ex repellat, voluptatibus cumque.</td>
                        <td>
                          <h5>
                            <a href="#">
                              <i class="jam jam-pencil"></i>
                            </a>
                            <a href="#">
                              <i class="jam jam-trash text-danger"></i>
                            </a>
                          </h5>
                        </td>
                      </tr>
                      <tr>
                        <th scope="col">15</th>
                        <td>Иванов Иван Иванович</td>
                        <td>ООО "Зе бест зубная клиника"</td>
                        <td>Петров Петр Петрович</td>
                        <td>02.09.2019</td>
                        <td>
                          <span class="zub-order-progress bg-success mr-2"></span>Выполнен
                        </td>
                        <td>-</td>
                        <td>
                          <h5>
                            <a href="#">
                              <i class="jam jam-pencil"></i>
                            </a>
                            <a href="#">
                              <i class="jam jam-trash text-danger"></i>
                            </a>
                          </h5>
                        </td>
                      </tr>
                    </tbody>
                  </table>
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
export default {
  name: "OrdersPage",
  components: {
    LNav, 
    LHeader, 
    LFooter,
  },
  data() {
    return {
      buttons: [
        {
          text: "Добавить",
          click: event => {
            event.preventDefault();
            this.$router.push("/orders/add/");
            return false;
          }
        }
      ]
    };
  }
};
</script>

<style>
</style>