using Microsoft.EntityFrameworkCore;

using Microsoft.Extensions.DependencyInjection;

using spec1.Models;
using System.Collections.Generic;
using System.Reflection.Emit;


namespace spec1.Data
{
    public class HarddataContext : DbContext
    {     

        public HarddataContext(DbContextOptions<HarddataContext> options) : base(options)
        {

        }
        public DbSet<spec1.Models.Harddata> Harddata { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Harddata>().ToTable("cpuhardinfo_2017");
        }
    }
}
