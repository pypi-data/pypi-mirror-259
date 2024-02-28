#ifndef MPART_UTILITIES_MISCELLANEOUS_H
#define MPART_UTILITIES_MISCELLANEOUS_H

#include <Kokkos_Core.hpp>
#include <unordered_map>
#include <string>

namespace mpart{

    template<typename T>
    KOKKOS_INLINE_FUNCTION void simple_swap(T& t1, T& t2) {
        T temp(t1);
        t1 = t2;
        t2 = temp;
    }

    /** Tries to read an options from a std::map.  If the key does not exist, the specified default value is returned. */
    std::string GetOption(std::unordered_map<std::string,std::string> const& map,
                          std::string                                 const& key,
                          std::string                                 const& defaultValue);

    /** Provides a mechanism for raising exceptions in CPU code where recovery is possible 
        and assertions in GPU code where exceptions aren't alllowed.
     */
    template<typename MemorySpace, typename ErrorType>
    struct ProcAgnosticError {
        static void error(const char*) {
            assert(false);
        }
    };

    template<typename ErrorType>
    struct ProcAgnosticError<Kokkos::HostSpace, ErrorType> {
        static void error(const char* message) {
            throw ErrorType(message);
        }
    };
}

#endif