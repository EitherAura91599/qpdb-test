package auth

type User struct {
	ID       uint   `gorm:"primaryKey"`
	Email    string `gorm:"unique; not null"`
	Username string `gorm:"unique; not null"`
	Password string
}
