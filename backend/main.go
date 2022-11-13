package main

import (
	"net/http"
	"github.com/gin-gonic/gin"
	"backend/lib"
	"os"
	"log"
)

type Ingredient struct {
	Quantity float32 `json:"quantity"`
	Unit string `json:"unit"`
	Name string `json:"name"`
}

type Recipe struct {
	Name string `json:name`
	IngredientList []Ingredient `json:"ingredient_list"`
	Instructions []string  `json:"instructions"`
}

var recipes map[string]Recipe

// init function is a reserved function name that gets called 1x no matter no matter how many times package is imported
func init() {
	var sugar_ingredient = Ingredient{ Quantity: 1.0, Unit: "cup", Name: "sugar"}
	var ingredients = []Ingredient {sugar_ingredient}
	var instructions_list = []string {"melt butter", "bake"}
	var best_recipe = Recipe{ Name: "test", IngredientList: ingredients, Instructions:  instructions_list}
	recipes = map[string]Recipe{"best_recipe": best_recipe, "best_recipe_2": best_recipe}

}


func greet(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, "Hello World!")
}


func getRecipeById(c *gin.Context){
	id := c.Param("id")

    // Loop over the list of recipes, looking for
    // an recipe whose ID value matches the parameter.
    for k, v := range recipes {
        if k == id {
            c.IndentedJSON(http.StatusOK, v)
            return
        }
    }
    c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Recipe not found"})
}


func getRecipeByName(c *gin.Context){
	id := c.Param("name")

    // Loop over the list of albums, looking for
    // an album whose ID value matches the parameter.
    for _, v := range recipes {
        if v.Name == id {
            c.IndentedJSON(http.StatusOK, v)
            return
        }
    }
    c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Recipe not found"})
}

func addRecipe(c *gin.Context) {
	var newRecipe Recipe

    // Call BindJSON to bind the received JSON to
    // newRecipe
    if err := c.BindJSON(&newRecipe); err != nil {
        return
    }
		recipes[newRecipe.Name] = newRecipe
    c.IndentedJSON(http.StatusCreated, newRecipe)
}


func uploadRecipe(c *gin.Context) {
	f, err := c.FormFile("file_input")
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{
				"error": err.Error(),
			})
			return
		}

		blobFile, err := f.Open()
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{
				"error": err.Error(),
			})
			return
		}

		err = lib.Uploader.UploadFile(blobFile, f.Filename)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{
				"error": err.Error(),
			})
			return
		}

		c.JSON(200, gin.H{
			"message": "success",
		})
	}

func main() {
	router := gin.Default()
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
		log.Printf("Defaulting to port %s", port)
	}
	router.GET("/", greet)
	router.GET("/recipe/:id", getRecipeById)
	router.GET("/recipe/name/:name", getRecipeByName)
	router.POST("/recipe", addRecipe)
	router.POST("/upload", uploadRecipe)
	http.Handle("/", router)
	router.Run("127.0.0.1:" + port)
}

