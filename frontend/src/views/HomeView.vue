<script>
// import TheWelcome from "../components/TheWelcome.vue";
import { useRecipeStore } from "@/stores/RecipeStore";

export default {
  setup() {
    const RecipeStore = useRecipeStore();

    return {
      RecipeStore,
    };
  },
  // components: { TheWelcome },
};
</script>

<template>
  <main>
    <!-- https://quasar.dev/vue-components/list-and-list-items -->
    <div class="recipes">
      <q-list dark bordered separator style="max-width: 350x">
        <q-item v-for="(recipe, index) in RecipeStore.allRecipes" :key="index">
          <!-- q-item-section not needed but is nice for formatting -->
          <q-item-section>
            <RouterLink to="/recipe">{{ recipe }}</RouterLink>
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </main>
</template>
