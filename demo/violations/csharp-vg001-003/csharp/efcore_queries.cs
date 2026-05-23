using Microsoft.EntityFrameworkCore;

namespace ValkGuardExample.Demo;

public sealed class CSharpViolationQueries
{
    public void RawSqlViolations(DbContext db)
    {
        db.Database.ExecuteSqlRaw("SELECT * FROM users LIMIT 1");
        db.Database.ExecuteSqlRaw("UPDATE users SET active = false");
        db.Database.ExecuteSqlRaw("DELETE FROM orders");
    }
}
