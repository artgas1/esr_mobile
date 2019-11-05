<template>
  <div class="sidebar" data-color="primary">
    <div class="logo">
      <a href="#" class="simple-text logo-mini">Zub</a>
      <a href="#" class="simple-text logo-normal">Dental Lab</a>
      <div class="navbar-minimize">
        <button id="minimizeSidebar" class="btn btn-simple btn-icon btn-neutral btn-round">
          <i class="now-ui-icons text_align-center visible-on-sidebar-regular"></i>
          <i class="now-ui-icons design_bullet-list-67 visible-on-sidebar-mini"></i>
        </button>
      </div>
    </div>
    <div class="sidebar-wrapper" id="sidebar-wrapper">
      <div class="user">
        <div class="photo">
          <img
            src="https://informatics.ru/images/cms/thumbs/8bb2374788957084defc0966234601d6b33d32f6/smirnov_175_175_2_80.jpg"
          />
        </div>
        <div class="info">
          <a>
            <span>Андрей Смирнов</span>
          </a>
        </div>
      </div>
      <ul class="nav">
        <li :class="currentMenuItem === 'home' ? 'active' : ''">
          <router-link to="/">
            <i class="jam jam-home"></i>
            <p>Главная</p>
          </router-link>
        </li>
        <li :class="currentMenuItem === 'orders' ? 'active' : ''">
          <router-link to="/orders">
            <i class="jam jam-document"></i>
            <p>Наряды</p>
          </router-link>
        </li>
        <li :class="currentMenuItem === 'stock' ? 'active' : ''">
          <router-link to="/stock">
            <i class="jam jam-box"></i>
            <p>Склад</p>
          </router-link>
        </li>
        <li :class="currentMenuItem === 'books' ? 'active' : ''">
          <router-link to="/books">
            <i class="jam jam-book"></i>
            <p>Справочники</p>
          </router-link>
        </li>
        <li :class="currentMenuItem === 'reports' ? 'active' : ''">
          <router-link to="/reports">
            <i class="jam jam-pie-chart"></i>
            <p>Отчеты</p>
          </router-link>
        </li>
        <li :class="currentMenuItem === 'settings' ? 'active' : ''">
          <router-link to="/settings">
            <i class="jam jam-cog"></i>
            <p>Настройки</p>
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "LNav",
  props: {
    currentMenuItem: {
      type: String
    }
  }
};
</script>

<style>
</style>