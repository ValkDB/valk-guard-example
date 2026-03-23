using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;

namespace ValkGuardExample.Data;

/// <summary>
/// Example repository demonstrating clean EF Core raw SQL usage.
/// All queries here should pass valk-guard with 0 findings.
/// </summary>
public class UserRepository
{
    private readonly AppDbContext _db;

    public UserRepository(AppDbContext db)
    {
        _db = db;
    }

    /// <summary>Safe: bounded SELECT with WHERE and LIMIT.</summary>
    public void GetActiveUserCount()
    {
        _db.Database.ExecuteSqlRaw(
            "SELECT count(*) FROM users WHERE active = true");
    }

    /// <summary>Safe: DELETE with WHERE clause.</summary>
    public async Task CleanupExpiredSessions()
    {
        await _db.Database.ExecuteSqlRawAsync(
            @"DELETE FROM orders
              WHERE status = 'expired'
                AND created_at < NOW() - INTERVAL '90 days'");
    }

    /// <summary>Safe: parameterized UPDATE with WHERE.</summary>
    public void DeactivateUser(int userId)
    {
        _db.Database.ExecuteSqlRaw(
            "UPDATE users SET active = false WHERE id = {0}", userId);
    }

    /// <summary>Safe: interpolated DELETE with WHERE.</summary>
    public async Task RemoveUser(int userId)
    {
        await _db.Database.ExecuteSqlInterpolatedAsync(
            $"DELETE FROM users WHERE id = {userId}");
    }
}
