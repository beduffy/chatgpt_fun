const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const world = new CANNON.World();
world.gravity.set(0, -9.82, 0);
world.broadphase = new CANNON.NaiveBroadphase();
world.solver.iterations = 10;

const groundMaterial = new CANNON.Material('ground');
const groundShape = new CANNON.Plane();
const groundBody = new CANNON.Body({ mass: 0, material: groundMaterial });
groundBody.addShape(groundShape);
groundBody.quaternion.setFromAxisAngle(new CANNON.Vec3(1, 0, 0), -Math.PI / 2);
world.addBody(groundBody);

const groundGeometry = new THREE.PlaneGeometry(1000, 1000);
// const groundTexture = new THREE.TextureLoader().load('textures/ground.jpg');
loader = new THREE.TextureLoader()
loader.crossOrigin = null 
// const groundTexture = loader.load('ground.jpg');
const groundTexture = loader.load('textures/ground.jpg');
groundTexture.wrapS = groundTexture.wrapT = THREE.RepeatWrapping;
groundTexture.repeat.set(50, 50);
const groundMaterial3D = new THREE.MeshLambertMaterial({ map: groundTexture });
const groundMesh = new THREE.Mesh(groundGeometry, groundMaterial3D);
groundMesh.rotation.x = -Math.PI / 2;
scene.add(groundMesh);

// Skybox
// const skyboxGeometry = new THREE.CubeGeometry(1000, 1000, 1000);
// const skyboxTextures = [
// 'skybox/right.jpg', 'skybox/left.jpg',
// 'skybox/top.jpg', 'skybox/bottom.jpg',
// 'skybox/front.jpg', 'skybox/back.jpg'
// ];
// const skyboxMaterials = skyboxTextures.map(texture => new THREE.MeshBasicMaterial({ map: new THREE.TextureLoader().load(texture), side: THREE.BackSide }));
// const skyboxMesh = new THREE.Mesh(skyboxGeometry, skyboxMaterials);
// scene.add(skyboxMesh);

// Lighting
const ambientLight = new THREE.AmbientLight(0x404040);
scene.add(ambientLight);
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
directionalLight.position.set(1, 1, 1);
scene.add(directionalLight);


// 4. Create the tank and control mechanics:
// export default class Tank {
//     constructor() {
//       // Tank constructor code...
//     }
  
//     // Tank methods...
//   }

// // Tank
// const tank = new Tank();
// tank.addToWorld(world);
// scene.add(tank.mesh);

// Controls
// const controls = new TankControls(tank, camera, renderer.domElement);
// controls.enable();

// Bullets
const bullets = [];
const bulletSpeed = 50;

const monkeyGeometry = new THREE.BoxGeometry(2, 2, 2);
const monkeyMaterial = new THREE.MeshLambertMaterial({ color: 0xff0000 });
const monkeyCount = 10;
const monkeys = [];

for (let i = 0; i < monkeyCount; i++) {
  const monkeyMesh = new THREE.Mesh(monkeyGeometry, monkeyMaterial);
  monkeyMesh.position.set(Math.random() * 100 - 50, 1, Math.random() * 100 - 50);
  scene.add(monkeyMesh);

  const monkeyShape = new CANNON.Box(new CANNON.Vec3(1, 1, 1));
  const monkeyBody = new CANNON.Body({ mass: 1 });
  monkeyBody.addShape(monkeyShape);
  monkeyBody.position.copy(monkeyMesh.position);
  world.addBody(monkeyBody);

  monkeys.push({ mesh: monkeyMesh, body: monkeyBody });
  }
  
  // Collision handling
  world.addEventListener('beginContact', (event) => {
  const bulletIndex = bullets.findIndex(bullet => bullet.body === event.bodyA || bullet.body === event.bodyB);
  if (bulletIndex === -1) return;
  const monkeyIndex = monkeys.findIndex(monkey => monkey.body === event.bodyA || monkey.body === event.bodyB);
  if (monkeyIndex === -1) return;
  
  // Remove monkey and bullet from the scene and world
  scene.remove(monkeys[monkeyIndex].mesh);
  world.removeBody(monkeys[monkeyIndex].body);
  monkeys.splice(monkeyIndex, 1);
  
  scene.remove(bullets[bulletIndex].mesh);
  world.removeBody(bullets[bulletIndex].body);
  bullets.splice(bulletIndex, 1);
  });
  
  // Animation loop
  function animate() {
  requestAnimationFrame(animate);
  
  const delta = clock.getDelta();
  
  // Update controls
  controls.update(delta);
  
  // Update bullets
  for (const bullet of bullets) {
  bullet.body.position.x += bulletSpeed * delta * bullet.direction.x;
  bullet.body.position.z += bulletSpeed * delta * bullet.direction.z;
  bullet.mesh.position.copy(bullet.body.position);
  }
  
  // Update monkeys
  for (const monkey of monkeys) {
  monkey.mesh.position.copy(monkey.body.position);
  monkey.mesh.quaternion.copy(monkey.body.quaternion);
  }
  
  // Update physics
  world.step(delta);
  
  // Render scene
  renderer.render(scene, camera);
  }
  
  animate();