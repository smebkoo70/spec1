using Microsoft.EntityFrameworkCore;

using Microsoft.Extensions.DependencyInjection;
using spec1.Data;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

//�·�ָ������汾��mysql����ʹ��new MySqlServerVersion(new Version())���ǿ��Եģ�
//builder.Services.AddDbContext<StudentContext>(options =>
//options.UseMySql(builder.Configuration.GetConnectionString("MysqlConnection"), new MySqlServerVersion("8.0.30")));
builder.Services.AddDbContext<UserContext>(options =>
  options.UseMySql(builder.Configuration.GetConnectionString("MysqlConnection"), new MySqlServerVersion("5.7.24")));

builder.Services.AddDbContext<HarddataContext>(options =>
  options.UseMySql(builder.Configuration.GetConnectionString("SpecConnection"), new MySqlServerVersion("5.7.24")));


var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
