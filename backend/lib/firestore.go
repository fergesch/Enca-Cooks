package lib

import (
	"cloud.google.com/go/firestore"
	"context"
	"fmt"
        "google.golang.org/api/iterator"
)

// https://cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest#cloud_google_com_go_firestore_DocumentSnapshot

func Test_firestore() {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, "enca-cooks")
	if err != nil {
		fmt.Println("I broke")
	}

	// recipes = client.Collection("recipes_test")

	fmt.Println("All recipes:")
	iter := client.Collection("recipes_test").Documents(ctx)
	for {
		doc, err := iter.Next()
		if err == iterator.Done {
			break
		}
		if err != nil {
			// return err
                        return
		}
		fmt.Println(doc.Data())
	}

        fmt.Println("Another Print")
        iter2 := client.Collection("recipes_test").Select("ingredients", "instructions").Documents(ctx)
	for {
		doc, err := iter2.Next()
		if err == iterator.Done {
			break
		}
		if err != nil {
			// return err
                        return
		}
                fmt.Println(doc.Ref.ID)
		fmt.Println(doc.Data())
	}

}
