using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace spec1.Models
{
    public class Harddata : PagingModel
    {
        [Key]
        public int Id { get; set; }
        public string Cpuname { get; set; }
        public string Maxmhz { get; set; }
        public string Nominal { get; set; }
        public string Enabled { get; set; }
        public string Orderable { get; set; }
        public string Cachel1 { get; set; }
        public string L2 { get; set; }
        public string L3 { get; set; }
        public string Cacheother { get; set; }
        public string Memory { get; set; }
        public string Other { get; set; }
        public string Storage { get; set; }
        public string Htmlpath { get; set; }

        public Harddata() { }


        public Harddata(int id, string cpuname, string maxmhz, string nominal, string enabled, string orderable, string cachel1, string l2, string l3, string cacheother, string memory, string other, string storage, string htmlpath)
        {
            Id = id;
            Cpuname = cpuname;
            Maxmhz = maxmhz;
            Nominal = nominal;
            Enabled = enabled;
            Orderable = orderable;
            Cachel1 = cachel1;
            L2 = l2;
            L3 = l3;
            Cacheother = cacheother;
            Memory = memory;
            Other = other;
            Storage = storage;
            Htmlpath = htmlpath;
        }


    }
}
