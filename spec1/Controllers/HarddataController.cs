using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using spec1.Data;
using spec1.Models;

namespace spec1.Controllers
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



    public class HarddataController : Controller
    {

        private readonly HarddataContext _harddataContext;


        //public IList<Harddata> listdata { get; set; }
        public List<Harddata> listdata { get; set; }

        page page1 = new page();

        public HarddataController(HarddataContext context)
        {
            _harddataContext = context;
        }



        [HttpGet]
        public async Task<IActionResult> Index()
        {
            //listdata = _harddataContext.Harddata.ToListAsync();
            

            try
            {

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
            //int cnt = _harddataContext.Set<Harddata>().Count();
            page1.TotalRecords =_harddataContext.Set<Harddata>().Count<Harddata>();
            int count = _harddataContext.Set<Harddata>().Count();
            GC.Collect();
            ViewBag.P = page1.P; 
            ViewBag.S = page1.S;
            ViewBag.TotalRecords = page1.TotalRecords;
            //ViewBag["page"] = page1;
            ViewBag.page = page1;
            return View(await _harddataContext.Set<Harddata>()
                                               .AsNoTracking()
                                               
                                               .Skip((page1.P - 1) * page1.S)
                                               .Take(page1.S)
                                               .ToListAsync()) ;
            
            //return View(await _harddataContext.Harddata.ToListAsync());
            //return View();
        }

        //total number of records
        public int TotalRecords { get; set; } = 0;

        
    }
}
