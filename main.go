package main

import (
	"log"
	"os"

	"github.com/gin-gonic/gin"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"

	"qpdb-test/auth"
)

func main() {
	dsn := "host=localhost user=admin password=Password123 dbname=qp-testdb port=5432 sslmode=disable"
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		log.Fatal("Failed to connect to DB:", err)
	}

	auth.Init(db) // initializes auth DB and automigrates User

	router := gin.Default()
	router.POST("/register", auth.Register)
	router.POST("/login", auth.Login)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	router.Run(":" + port)
}
