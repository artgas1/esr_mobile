<template>
  <div>
    <div class="text-center p-4 text-muted" v-if="!selectedItems.length">{{noItemsText}}</div>
    <div class v-if="selectedItems.length">
      <div v-for="item in selectedItems" v-bind:key="item.idx" class="d-flex align-items-center">
        <div class="w-100">
          <slot name="itemRow" v-bind:item="item"></slot>
        </div>
        <div class="ml-auto text-right">
          <a href="#" @click="removeItem($event, item)">
            <span class="jam jam-trash"></span>
          </a>
        </div>
      </div>
    </div>
    <button
      class="btn btn-primary w-100"
      @click="modalShown = true"
      v-if="!single || !selectedItems.length"
    >{{addItemText}}</button>
    <div
      ref="modal"
      class="modal"
      tabindex="-1"
      role="dialog"
      v-if="!single || !selectedItems.length"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{addItemText}}</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Закрыть"
              @click="modalShown = false"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <input
              type="text"
              class="form-control"
              :placeholder="addItemInputPlaceholder"
              v-model="searchQuery"
            />
            <div class="shadow mx-3">
              <a
                href="#"
                @click="addItem($event, item); modalShown = false; searchQuery = ''"
                v-for="item in suggestedItems"
                v-bind:key="item.id"
                class="d-block p-2"
              >
                <slot name="addItemRow" v-bind:item="item"></slot>
              </a>
              <p
                v-if="searchQuery && !suggestedItems.length"
                class="text-center p-4 text-muted"
              >Ничего не найдено</p>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-dismiss="modal"
              @click="modalShown = false"
            >Отмена</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StableIndexArray from "../../StableIndexArray";
let $ = window.$;
let itemsList = new StableIndexArray();
export default {
  name: "LList",
  props: {
    noItemsText: {
      type: String,
      default: "Нет элементов"
    },
    items: {
      type: Array,
      default: () => []
    },
    suggestedItemsFilter: {
      type: Function
    },
    addItemText: {
      type: String,
      default: "Добавить"
    },
    addItemInputPlaceholder: {
      type: String,
      default: "Добавить"
    },
    single: {
      type: Boolean,
      default: false
    },
    unique: {
      type: Boolean,
      default: false
    }, 
    uniqueItemsFilter: {
      type: Function, 
      default: () => true,
    }
  },
  data() {
    return {
      modalShown: false,
      searchQuery: "",
      selectedItems: []
    };
  },
  computed: {
    suggestedItems() {
      let suggested = [];
      if (this.searchQuery.length) {
        suggested = this.allItems.filter(elem =>
          this.suggestedItemsFilter(elem, this.searchQuery)
        );
      }
      if (this.unique) {
        suggested = suggested.filter(elem =>
          this.uniqueItemsFilter(elem, this.selectedItems)
        );
      }
      return suggested.slice(0, 10);
    }
  },
  watch: {
    modalShown() {
      $(this.$refs.modal).modal(this.modalShown ? "show" : "hide");
    }
  },
  created() {
    if (this.items.length) {
      itemsList = new StableIndexArray(this.items);
    }
    this.$on("all-items-available", items => {
      this.allItems = items;
    });
  },
  methods: {
    emitChangeEvent() {
      this.selectedItems = itemsList.existing();
      window.console.log(itemsList);
      if (this.single) {
        this.$emit(
          "change",
          this.selectedItems.length ? this.selectedItems[0] : null
        );
      } else {
        this.$emit("change", this.selectedItems);
      }
    },
    addItem(event, item) {
      event.preventDefault();
      itemsList.push(item);
      this.emitChangeEvent();
      return false;
    },
    removeItem(event, item) {
      event.preventDefault();
      itemsList.remove(item);
      this.emitChangeEvent();
      return false;
    }
  }
};
</script>

<style>
</style>