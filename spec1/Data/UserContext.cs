using Microsoft.EntityFrameworkCore;

using Microsoft.Extensions.DependencyInjection;

using spec1.Models;
using System.Collections.Generic;
using System.Reflection.Emit;

namespace spec1.Data
{
    public class UserContext : DbContext
    {
        public UserContext(DbContextOptions<UserContext> options) : base(options)
        {
        }
        public DbSet<spec1.Models.User> User { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<User>().ToTable("user");
        }
    }
}
