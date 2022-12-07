using Microsoft.AspNetCore.Mvc;

namespace spec1.Models
{
    public class page
    {
        [BindProperty(SupportsGet = true)]
        public int P { get; set; } = 1;

        //page size variable
        [BindProperty(SupportsGet = true)]
        public int S { get; set; } = 10;

        public int TotalRecords { get; set; } = 0;

    }
}
