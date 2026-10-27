<?php
declare(strict_types=1);

const COURSE_PATH = '/cours/conception-audio-video/';
const ACCESS_DURATION = 14400;
const MAX_ATTEMPTS = 5;
const LOCK_DURATION = 300;

header('Cache-Control: no-store, private, max-age=0');
header('Pragma: no-cache');
header('X-Robots-Tag: noindex, nofollow, noarchive');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: same-origin');
header("Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; img-src 'self'; form-action 'self'; base-uri 'none'; frame-ancestors 'self'");

session_name('inseec_course');
ini_set('session.use_strict_mode', '1');
session_set_cookie_params([
    'lifetime' => 0,
    'path' => COURSE_PATH,
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Lax',
]);
if (!session_start()) {
    http_response_code(503);
    exit('Accès temporairement indisponible.');
}
$expectedHash = require __DIR__ . '/access-config.php';
if (!is_string($expectedHash) || !preg_match('/\A[a-f0-9]{64}\z/', $expectedHash)) {
    http_response_code(503);
    exit('Accès temporairement indisponible.');
}
if (!isset($_SESSION['csrf'])) {
    $_SESSION['csrf'] = bin2hex(random_bytes(24));
}
$now = time();
$authenticated = isset($_SESSION['until'], $_SESSION['code_version'])
    && (int) $_SESSION['until'] > $now
    && hash_equals($expectedHash, (string) $_SESSION['code_version']);
$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $csrf = $_POST['csrf'] ?? '';
    if (!is_string($csrf) || !hash_equals($_SESSION['csrf'], $csrf)) {
        http_response_code(403);
        $error = 'La session a expiré. Réessaie avec le formulaire ci-dessous.';
    } else {
        // Un compteur persistant par adresse IP empêche de contourner la limite
        // en supprimant les cookies. Le fichier reste hors de la racine du site.
        $key = hash('sha256', __DIR__ . '|' . ($_SERVER['REMOTE_ADDR'] ?? 'unknown'));
        $file = sys_get_temp_dir() . '/inseec-access-' . $key . '.json';
        $handle = @fopen($file, 'c+');
        if ($handle === false || !flock($handle, LOCK_EX)) {
            if (is_resource($handle)) fclose($handle);
            http_response_code(503);
            $error = 'La connexion est temporairement indisponible. Réessaie plus tard.';
        } else {
            @chmod($file, 0600);
            $state = json_decode(stream_get_contents($handle), true);
            if (!is_array($state) || !isset($state['since'], $state['attempts'])
                || $now - (int) $state['since'] >= LOCK_DURATION) {
                $state = ['since' => $now, 'attempts' => 0];
            }
            if ((int) $state['attempts'] >= MAX_ATTEMPTS) {
                http_response_code(429);
                header('Retry-After: ' . max(1, LOCK_DURATION - ($now - (int) $state['since'])));
                $error = 'Trop de tentatives. Patiente cinq minutes avant de réessayer.';
            } else {
                $code = $_POST['code'] ?? '';
                if (is_string($code) && preg_match('/\A[0-9]{4}\z/', $code)
                    && hash_equals($expectedHash, hash('sha256', $code))) {
                    session_regenerate_id(true);
                    $_SESSION['until'] = $now + ACCESS_DURATION;
                    $_SESSION['code_version'] = $expectedHash;
                    $_SESSION['csrf'] = bin2hex(random_bytes(24));
                    $authenticated = true;
                    $state = ['since' => $now, 'attempts' => 0];
                } else {
                    $state['attempts'] = (int) $state['attempts'] + 1;
                    http_response_code(401);
                    $error = 'Ce code est incorrect. Réessaie.';
                }
            }
            rewind($handle);
            ftruncate($handle, 0);
            fwrite($handle, json_encode($state));
            fflush($handle);
            flock($handle, LOCK_UN);
            fclose($handle);
            if ($authenticated) {
                session_write_close();
                header('Location: ' . COURSE_PATH, true, 303);
                exit;
            }
        }
    }
}

$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$path = is_string($uri) ? rawurldecode($uri) : '';
if (strncmp($path, COURSE_PATH, strlen(COURSE_PATH)) !== 0) {
    http_response_code(404);
    exit('Page introuvable.');
}
$resource = substr($path, strlen(COURSE_PATH));
if ($resource === '' || $resource === 'index.html' || $resource === 'access.php') {
    $resource = 'index.html';
}
$allowed = ['index.html' => 'text/html; charset=UTF-8',
    'style.css' => 'text/css; charset=UTF-8',
    'app.js' => 'text/javascript; charset=UTF-8'];
if (preg_match('/\Aassets\/diapo-(?:0[1-9]|[1-6][0-9]|7[0-7])\.jpg\z/', $resource)) {
    $allowed[$resource] = 'image/jpeg';
}
if (!isset($allowed[$resource])) {
    http_response_code(404);
    exit('Page introuvable.');
}
if ($authenticated) {
    session_write_close();
    header('Content-Type: ' . $allowed[$resource]);
    readfile(__DIR__ . '/' . $resource);
    exit;
}
if ($resource !== 'index.html') {
    session_write_close();
    http_response_code(403);
    header('Content-Type: text/plain; charset=UTF-8');
    exit('Saisis le code sur la page du cours pour accéder à cette ressource.');
}
header('Content-Type: text/html; charset=UTF-8');
$csrfToken = htmlspecialchars($_SESSION['csrf'], ENT_QUOTES, 'UTF-8');
session_write_close();
?>
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Accéder au cours · Audio & vidéo</title>
<style>
*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:#f7f8f5;color:#122d38;font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;padding:24px}.card{width:100%;max-width:440px;background:white;border:1px solid #dce3de;border-radius:16px;padding:38px}.logo{display:grid;place-items:center;background:#122d38;color:#d5ed72;font-weight:800;width:46px;height:46px;border-radius:50%;font-size:23px}.eyebrow{font-size:10px;letter-spacing:2px;color:#617e3d;margin:28px 0 12px}h1{font-size:32px;line-height:1.15;letter-spacing:-1px;margin:0 0 18px}p{color:#627078;font-size:14px}label{display:block;font-size:13px;font-weight:600;margin:24px 0 8px}input{width:100%;min-height:58px;border:1px solid #aebfb4;border-radius:6px;text-align:center;letter-spacing:14px;padding:10px 10px 10px 24px;font:28px monospace}button{width:100%;border:0;border-radius:6px;background:#122d38;color:white;padding:15px;font:600 14px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;margin-top:16px;cursor:pointer}input:focus,button:focus{outline:3px solid #d5ed72;outline-offset:3px}.error{color:#a43131;background:#fff1ee;padding:12px;border-radius:5px;font-size:13px}.meta{font-size:11px;border-top:1px solid #e5eae3;padding-top:18px;margin-top:25px}@media(max-width:400px){.card{padding:26px}h1{font-size:28px}}
</style></head><body><main class="card"><div class="logo">ng.</div><div class="eyebrow">ESPACE ÉTUDIANTS · INSEEC</div><h1>Conception<br>audio & vidéo.</h1><p>Saisis le code communiqué par ton formateur pour retrouver le cours et ses ressources.</p>
<?php if ($error !== ''): ?><p class="error" role="alert"><?php echo htmlspecialchars($error, ENT_QUOTES, 'UTF-8'); ?></p><?php endif; ?>
<form method="post" action="<?php echo COURSE_PATH; ?>"><input type="hidden" name="csrf" value="<?php echo $csrfToken; ?>"><label for="code">Code d’accès à 4 chiffres</label><input id="code" name="code" type="password" inputmode="numeric" pattern="[0-9]{4}" minlength="4" maxlength="4" autocomplete="off" required aria-describedby="code-help"><p id="code-help">L’accès reste ouvert pendant quatre heures sur ce navigateur.</p><button type="submit">Accéder au cours →</button></form><p class="meta">Nicolas Genaudet · INSEEC MSc2 MCSC · 18 heures</p></main></body></html>
