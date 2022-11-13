import { defineStore } from "pinia";
import { fiveLetter, toggleMatch, checkWord } from "../utils/Utils";
import Api from "../utils/Api.vue";
// import { ref, computed } from "vue";

export const useRecipeStore = defineStore("RecipeStore", {
  state: () => {
    return {
      currentWord: "",
      allRecipes: ["Brownies", "Lemon Bars", "Meatballs"],
      recoWord: {
        rnd_cnt: [],
        word: "",
        words: [],
      },
      showModal: false,
    };
  },

  // getters: {
  //   doubleCount: (state) => state.count * 2,
  // },

  actions: {
    changeMatch(loc) {
      // given position of letter [ith word, jth letter] want to flip between -1,0,1
      Object.values(this.words[loc[0]]).forEach((value) => {
        value.forEach(function (item) {
          if (item[0] == loc[1]) {
            item[1] = toggleMatch(item[1]);
          }
        });
      });
    },

    async addWord() {
      let word = fiveLetter(this.currentWord.slice());
      if (word) {
        let check = await checkWord(word);
        if (check) {
          let letterList = word.split("");

          const letterMap = {};
          letterList.forEach(function (item, index) {
            if (!(item in letterMap)) {
              letterMap[item] = [];
            }
            letterMap[item].push([index, -1]);
          });

          this.words.push(letterMap);
          this.currentWord = ""; //set back to empty for next input
        } else {
          this.showModal = true;
        }
      } else {
        this.showModal = true;
      }
    },

    removeWord(n) {
      let wordList = [...this.words];
      wordList.splice(n, 1);
      this.words = wordList;
    },

    getWord() {
      Api.post("/word", this.words)
        .then((response) => {
          // console.log(response)
          this.recoWord = response["data"];
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
});
