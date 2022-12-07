using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using spec1.Data;
using System.Linq;

namespace spec1.Controllers
{
    public class UserController : Controller
    {

        private readonly UserContext _userContext;

        public UserController(UserContext context)
        {
            _userContext = context;
        }
        public async Task<IActionResult>  Index()
        {
            return View(await _userContext.User.ToListAsync());
            //return View();
        }
    }
}
