using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace spec1.Controllers
{
    public class Hard2Controller : Controller
    {
        // GET: Hard2Controller
        public ActionResult Index()
        {
            return View();
        }

        // GET: Hard2Controller/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

        // GET: Hard2Controller/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Hard2Controller/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }

        // GET: Hard2Controller/Edit/5
        public ActionResult Edit(int id)
        {
            return View();
        }

        // POST: Hard2Controller/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(int id, IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }

        // GET: Hard2Controller/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: Hard2Controller/Delete/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(int id, IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }
    }
}
