<template>
  <div id="wrapper">
    <l-nav current-menu-item="books"></l-nav>
    <div class="main-panel" id="main-panel">
      <l-header title="Справочники" />
      <div class="content">
        <div class="row">
          <div v-for="book in books" v-bind:key="book.title" class="col-12 col-md-6 col-lg-4">
            <router-link :to="book.link" class="text-decoration-none">
              <div class="card bg-primary text-white text-center shadow-lg py-5">
                <h4 class="card-title mt-0">{{book.title}}</h4>
                <span :class="book.iconClass"></span>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LNav from "./blocks/LNav";
import LHeader from "./blocks/LHeader";
export default {
  name: "BooksPage",
  components: {
    LNav,
    LHeader
  },
  data() {
    return {
      books: [
        {
          title: "Работы",
          link: "/books/works/",
          iconClass: "jam jam-cog"
        },
        {
          title: "Операции",
          link: "/books/operations/",
          iconClass: "jam jam-cog"
        },
        {
          title: "Материалы",
          link: "/books/materials/",
          iconClass: "jam jam-cog"
        },
        {
          title: "Техники",
          link: "/books/technicians/",
          iconClass: "jam jam-cog"
        },
        {
          title: "Клиники",
          link: "/books/clinics/",
          iconClass: "jam jam-cog"
        },
        {
          title: "Врачи",
          link: "/books/doctors/",
          iconClass: "jam jam-cog"
        }, 
        {
          title: "Прайс-листы работ", 
          link: "/books/pricelists/works/",
          iconClass: "jam jam-cog", 
        }, 
        {
          title: "Прайс-листы операций", 
          link: "/books/pricelists/operations/",
          iconClass: "jam jam-cog", 
        }
      ]
    };
  }
};
</script>

<style>
</style>