#include <string>


// This header is required to register plugins. It's good practice to place it
// in the cc file, like it's done here.
#include <gz/plugin/Register.hh>

// To use gzmsg printing methods 
#include <gz/common/Console.hh>


// Our plugin's header
#include "HelloWorldSystem.hpp"


GZ_ADD_PLUGIN(

    hello_world::HelloWorldSystem,
    gz::sim::System,
    hello_world::HelloWorldSystem::ISystemPostUpdate)

using namespace hello_world;

void HelloWorldSystem::PostUpdate(const gz::sim::UpdateInfo &_info,
    const gz::sim::EntityComponentManager &/*_ecm*/)
{

  // This is a simple example of how to get information from UpdateInfo.
  std::string msg = "Hello, world! Simulation is ";
  if (!_info.paused)
    msg += "not ";
  msg += "paused.";

  // Messages printed with gzmsg only show when running with verbosity 3 or
  // higher (i.e. gz sim -v 3)
  gzmsg << msg << std::endl;
}
