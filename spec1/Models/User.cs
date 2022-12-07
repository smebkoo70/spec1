using System.ComponentModel.DataAnnotations;


namespace spec1.Models
{
    public class User
    {
        public User(int id, string username, string password, string name, string type1)
        {
            Id = id;
            Username = username;
            Password = password;
            Name = name;
            Type1 = type1;
        }

        public User()
        {

        }

        [Key]
        public int Id { get; set; }
        public string Username { get; set; }
        public string Password { get; set; }
        public string Name { get; set; }
        public string Type1 { get; set; }
    }
}
