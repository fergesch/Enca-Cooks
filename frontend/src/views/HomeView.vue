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
      <q-list>
        <!-- <q-item v-for="(word,index) in RecipeStore.allRecipes" clickable v-ripple> -->
        <q-item v-for="(recipe, index) in RecipeStore.allRecipes" :key="index">
          <!-- q-item-section not needed but is nice for formatting -->
          <q-item-section>
            <RouterLink to="/newRecipe">{{ recipe }}</RouterLink>
          </q-item-section>
        </q-item>
      </q-list>
      <!-- <div v-for="(recipe, index) in wordStore.words" :key="index">
        <wordRow :wordMap="word" :n="index" />
      </div> -->
    </div>
  </main>
</template>
