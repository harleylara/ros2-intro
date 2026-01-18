#ifndef __GZ_PLUGINS_PLUGINS_HELLO_WORLD_HELLOWORLD_HPP__
#define __GZ_PLUGINS_PLUGINS_HELLO_WORLD_HELLOWORLD_HPP__

#include "gz/sim/System.hh"

namespace hello_world {

  class HelloWorldSystem:
    public gz::sim::System,
    public gz::sim::ISystemPostUpdate {

      public: void PostUpdate(const gz::sim::UpdateInfo &_info,
                  const gz::sim::EntityComponentManager &_ecm) override;

    };

}

#endif
